const divs = document.querySelectorAll(`nav > div`);

console.log(divs);

divs.forEach((e)=>{
    const span = e.querySelector(`span`);
    const underline = e.querySelector(`div`);

    span?.addEventListener(`mouseover`, ()=>{
        underline?.classList.add(`nav-animation`);
    });
    span?.addEventListener(`mouseout`, ()=>{
        underline?.classList.remove(`nav-animation`);
    });
});
