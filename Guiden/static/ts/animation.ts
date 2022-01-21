const divs = document.querySelectorAll(`nav > div.opt`);

console.log(divs);

divs.forEach((e)=>{
    const text = e.querySelector(`a`);
    const underline = e.querySelector(`.underline`);

    text?.addEventListener(`mouseover`, ()=>{
        underline?.classList.add(`nav-animation`);
    });
    text?.addEventListener(`mouseout`, ()=>{
        underline?.classList.remove(`nav-animation`);
    });
});
