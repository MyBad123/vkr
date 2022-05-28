// for item in shop 
function seeClick(e) {
    let baseObj = e.target;
    try {
        let obj = baseObj.querySelector('.shop-grid-item-btn');
        obj.classList.add('shop-grid-item-btn-opacity');
    } catch(e) {
        let newObj = baseObj.closest('.shop-grid-item').querySelector('.shop-grid-item-btn');
        newObj.classList.add('shop-grid-item-btn-opacity');
    }
}

function noSeeClick(e) {
    let baseObj = e.target;
    try {
        let obj = baseObj.querySelector('.shop-grid-item-btn');
        obj.classList.remove('shop-grid-item-btn-opacity');
    } catch(e) {
        let newObj = baseObj.closest('.shop-grid-item').querySelector('.shop-grid-item-btn');
        newObj.classList.remove('shop-grid-item-btn-opacity');
    }
}

for (let i of document.querySelectorAll('.shop-grid-item')) {
    i.addEventListener("mouseover", seeClick);
    i.addEventListener("mouseout", noSeeClick);
}
