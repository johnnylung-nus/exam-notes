'use strict';

const viewButtons = document.querySelectorAll('[data-view]');
let previewClosedDetails = [];
viewButtons.forEach((button) => {
  button.addEventListener('click', () => {
    const printView = button.dataset.view === 'print';
    if (printView && !document.body.classList.contains('print-view')) {
      previewClosedDetails = [...document.querySelectorAll('details:not([open])')];
      previewClosedDetails.forEach((item) => { item.open = true; });
    } else if (!printView) {
      previewClosedDetails.forEach((item) => { item.open = false; });
      previewClosedDetails = [];
    }
    document.body.classList.toggle('print-view', printView);
    viewButtons.forEach((item) => item.setAttribute('aria-pressed', String(item === button)));
  });
});

document.querySelector('#print-button')?.addEventListener('click', () => window.print());
const labels = document.querySelector('#diagram-labels');
document.querySelector('#toggle-labels')?.addEventListener('click', (event) => {
  const visible = event.currentTarget.getAttribute('aria-pressed') !== 'true';
  labels.classList.toggle('labels-hidden', !visible);
  event.currentTarget.setAttribute('aria-pressed', String(visible));
  event.currentTarget.textContent = visible ? 'Hide labels' : 'Show labels';
});

// Expand recall answers for printing, then restore the reader's previous state.
let closedDetails = [];
window.addEventListener('beforeprint', () => {
  closedDetails = [...document.querySelectorAll('details:not([open])')];
  closedDetails.forEach((item) => { item.open = true; });
});
window.addEventListener('afterprint', () => {
  closedDetails.forEach((item) => { item.open = false; });
  closedDetails = [];
});

const connectionButton = document.querySelector('#toggle-projections');
const connectionNote = document.querySelector('#projection-note');
connectionButton?.addEventListener('click', () => {
  const visible = connectionButton.getAttribute('aria-pressed') !== 'true';
  connectionButton.setAttribute('aria-pressed', String(visible));
  connectionButton.textContent = visible ? 'Hide the connection' : 'Show the connection';
  connectionNote.hidden = !visible;
});
