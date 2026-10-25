(function(root){'use strict';
const key='exam-notes-review-v1';
function empty(){return {version:1,reviewed:{},excluded:{},answers:{}}}
function parse(raw){try{const value=typeof raw==='string'?JSON.parse(raw):raw;if(!value||value.version!==1)return empty();return {version:1,reviewed:value.reviewed&&typeof value.reviewed==='object'?value.reviewed:{},excluded:value.excluded&&typeof value.excluded==='object'?value.excluded:{},answers:value.answers&&typeof value.answers==='object'?value.answers:{}}}catch{return empty()}}
function include(state,id){return state.excluded[id]!==true}
function setIncluded(state,id,on){if(on)delete state.excluded[id];else state.excluded[id]=true;return state}
function answerState(state,q){const a=state.answers[q.id];return a&&a.signature===q.signature&&Number.isInteger(a.choice)&&a.choice>=0&&a.choice<q.options.length?a:null}
function summary(state,questions){const attempted=questions.filter(q=>answerState(state,q));return {total:questions.length,attempted:attempted.length,correct:attempted.filter(q=>answerState(state,q).choice===q.answer).length}}
function record(state,q,choice){const previous=answerState(state,q);state.answers[q.id]={choice,signature:q.signature,attempts:(previous?.attempts||0)+1};return state}
function uniqueOrder(data){return [...new Set([...data.groups.flatMap(g=>g.lectures.flatMap(l=>l.entries.map(e=>e.conceptId))),...data.supplements.map(e=>e.conceptId),...Object.keys(data.concepts)])]}
function navigation(data,cid,requested){
const sequence=data.groups.flatMap(g=>g.lectures.flatMap(l=>[...new Set(l.entries.map(e=>e.conceptId))].filter(id=>data.concepts[id]).map(id=>({id,lecture:l.id,label:g.name+' → '+l.title}))));
const present=new Set(sequence.map(x=>x.id));
for(const id of uniqueOrder(data))if(data.concepts[id]&&!present.has(id)){sequence.push({id,lecture:null,label:'Additional concepts and sample-paper practice'});present.add(id)}
let i=sequence.findIndex(x=>x.id===cid&&x.lecture===requested);if(i<0)i=sequence.findIndex(x=>x.id===cid);if(i<0)return null;
let previous=i-1,next=i+1;while(previous>=0&&sequence[previous].id===cid)previous--;while(next<sequence.length&&sequence[next].id===cid)next++;
return {current:sequence[i],previous:sequence[previous]||null,next:sequence[next]||null};
}
const api={key,empty,parse,include,setIncluded,answerState,summary,record,uniqueOrder,navigation};if(typeof module!=='undefined'&&module.exports)module.exports=api;else root.ExamReviewState=api;
})(typeof window==='undefined'?{}:window);
