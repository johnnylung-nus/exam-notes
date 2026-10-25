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
const api={key,empty,parse,include,setIncluded,answerState,summary,record,uniqueOrder};if(typeof module!=='undefined'&&module.exports)module.exports=api;else root.ExamReviewState=api;
})(typeof window==='undefined'?{}:window);
