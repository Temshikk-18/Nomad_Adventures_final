document.addEventListener('DOMContentLoaded',()=>{
 const menu=document.querySelector('[data-menu]'),links=document.querySelector('[data-nav-links]');
 if(menu&&links) menu.addEventListener('click',()=>{links.classList.toggle('mobile-open');menu.setAttribute('aria-expanded',links.classList.contains('mobile-open'))});
 const picker=document.querySelector('[data-language-picker]'),trigger=document.querySelector('[data-language-trigger]');
 if(picker&&trigger){trigger.addEventListener('click',e=>{e.stopPropagation();picker.classList.toggle('open');trigger.setAttribute('aria-expanded',picker.classList.contains('open'))});document.addEventListener('click',()=>picker.classList.remove('open'));document.addEventListener('keydown',e=>{if(e.key==='Escape')picker.classList.remove('open')});}
 document.querySelectorAll('.filters').forEach(el=>{let x=0;el.addEventListener('touchstart',e=>x=e.touches[0].clientX,{passive:true});el.addEventListener('touchmove',e=>{const dx=x-e.touches[0].clientX;if(Math.abs(dx)>4)el.scrollLeft+=dx;x=e.touches[0].clientX},{passive:true})});
 const observer=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('is-visible');observer.unobserve(e.target)}}),{threshold:.08});
 document.querySelectorAll('.category-card,.region-tile,.tour-card,.place-card,.region-card-large').forEach(el=>{el.classList.add('reveal');observer.observe(el)});
});
