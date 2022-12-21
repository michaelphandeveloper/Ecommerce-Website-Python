var updateBtns = document.getElementsByClassName("update-cart");

for (i = 0; i < updateBtns.length; i++) {
  updateBtns[i].addEventListener("click", function () {
    var productId = this.dataset.product;
    var action = this.dataset.action;
    console.log("ID: ", productId, "Action: ", action);

    console.log("user: ", user);
    if (user === "AnonymousUser") {
      alert(1);
      //addCookieItem(productId, action)
    } else {
      alert(2);
      updateUserOrder(productId, action);
    }
  });
}

function addCookieItem(productId, action) {
  console.log("Not logged in...");

  if (action == "add") {
    if (cart[productId] == undefined) {
      cart[productId] = { quantity: 1 };
    } else {
      cart[productId]["quantity"] += 1;
    }
  }

  if (action == "remove") {
    cart[productId]["quantity"] -= 1;

    if (cart[productId]["quantity"] <= 0) {
      console.log("Item has been removed from your cart");
      delete cart[productId];
    }
  }
  console.log("Cart:", cart);
  document.cookie = "cart=" + JSON.stringify(cart) + ";domain=;path=/";
  location.reload();
}

function updateUserOrder(productId, action) {
  console.log("Logged in");

  var url = "/update_item/";

  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ productId: productId, action: action }),
  })
    .then((response) => {
      return response.json();
    })

    .then((data) => {
      console.log("data:", data);
      location.reload();
    });
}