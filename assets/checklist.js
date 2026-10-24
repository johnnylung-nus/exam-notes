"use strict";
const boxes=[...document.querySelectorAll('[data-checkpoint]')];
let saved={};try{saved=JSON.parse(localStorage.getItem('exam-checkpoints-v1')||'{}')}catch{}
function status(){document.querySelector('#check-status').textContent=boxes.filter(b=>b.checked).length+' checked on this device';}
boxes.forEach(box=>{box.checked=saved[box.dataset.checkpoint]===true;box.addEventListener('change',()=>{saved[box.dataset.checkpoint]=box.checked;try{localStorage.setItem('exam-checkpoints-v1',JSON.stringify(saved))}catch{}status();});});status();
document.querySelector('#concept-search').addEventListener('input',event=>{const query=event.target.value.toLowerCase();document.querySelectorAll('.concept-group').forEach(group=>{const rows=[...group.querySelectorAll('li')];rows.forEach(row=>row.hidden=!row.textContent.toLowerCase().includes(query));group.hidden=rows.every(row=>row.hidden);});});
