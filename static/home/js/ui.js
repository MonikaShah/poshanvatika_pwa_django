document.addEventListener('DOMContentLoaded', function() {
    // nav menu
    const menus = document.querySelectorAll('.side-menu');
    M.Sidenav.init(menus, {edge: 'right'});
    // add recipe form
    // M.Sidenav.init(forms, {edge: 'left'});
    // forms.addEventListener(click)

  });


  const add_btn = document.querySelector('.add-btn');
  const close_btn = document.querySelector('.close-btn');
  const form = document.querySelector('.side-form');

  function openCreatePostModal() {
    form.style.display = 'block';
    // console.log(form.style)
  }
  
  add_btn.addEventListener('click', openCreatePostModal);
  close_btn.addEventListener('click', ()=>{form.style.display = 'none'});
