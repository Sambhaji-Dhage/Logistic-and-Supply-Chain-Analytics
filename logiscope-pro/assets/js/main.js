// Mobile navigation toggle and basic form validation
(function(){
  const toggle = document.querySelector('#mobileToggle');
  const nav = document.querySelector('#primaryNav');
  if(toggle && nav){
    toggle.addEventListener('click', ()=>{
      nav.classList.toggle('open');
    });
  }

  // Simple required-field validation
  document.addEventListener('submit', (e)=>{
    const form = e.target;
    if(!(form instanceof HTMLFormElement)) return;
    const requiredFields = form.querySelectorAll('[required]');
    for(const field of requiredFields){
      if((field instanceof HTMLInputElement || field instanceof HTMLTextAreaElement) && !field.value.trim()){
        e.preventDefault();
        field.focus();
        alert('Please fill out all required fields.');
        break;
      }
    }
  });
})();