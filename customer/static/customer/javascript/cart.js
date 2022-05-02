let updateBtns = document.getElementsByClassName('update-cart')

for (let i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        let itemId = this.dataset.item
        let action = this.dataset.action
        let rid = this.dataset.rid
        console.log('itemId:', itemId, 'action:', action, 'rid:', rid)

        updateUserOrder(itemId, action, rid)
    })
}
/*
function addCookieItem(itemId, action){
    if(action == 'add'){
        if(cart[itemId] == undefined){
            cart[itemId] = {'quantity':1}
        }else{
            cart[itemId]['quantity'] += 1
        }
    }

    if(action=='remove'){
        cart[itemId]['quantity'] -= 1

        if(cart[itemId]['quantity'] <= 0){
            console.log('Remove item')
            delete cart[itemId]
        }
    }
    console.log('Cart:', cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
    location.reload()
}
*/ 

function updateUserOrder(itemId, action, rid){
    console.log("sending data..")

    let url = '../../update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken, 
        },
        body:JSON.stringify({'itemId': itemId, 'action': action, 'rid': rid, })
    })

    .then((response) =>{
        return response.json()
    })

    .then((data) => {
        console.log('data: ', data)
        location.reload()
    })
}