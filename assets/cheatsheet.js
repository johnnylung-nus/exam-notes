'use strict';
document.querySelector('#density').addEventListener('click',event=>{const compact=document.body.classList.toggle('compact');event.currentTarget.setAttribute('aria-pressed',String(compact));event.currentTarget.textContent=compact?'Standard screen view':'Compact screen view';});
document.querySelector('#print').addEventListener('click',()=>window.print());
