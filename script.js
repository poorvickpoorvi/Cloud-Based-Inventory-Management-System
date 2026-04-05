const API_URL = "arn:aws:sns:us-east-1:181777504105:Standard:5abc58f9-8aae-4813-9805-20c616776a50";

async function addProduct(){

    const product = {
        product_name: document.getElementById("name").value,
        category: document.getElementById("category").value,
        price: document.getElementById("price").value,
        stock: document.getElementById("stock").value,
        threshold: document.getElementById("threshold").value
    };

    await fetch(API_URL + "/add-product",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body: JSON.stringify(product)
    });

    alert("Product Added!");

    loadProducts();
}

async function loadProducts(){

    const response = await fetch(API_URL + "/products");

    const data = await response.json();

    const table = document.getElementById("productList");

    table.innerHTML="";

    data.forEach(product=>{

        const row = `
        <tr>
            <td>${product.product_name}</td>
            <td>${product.category}</td>
            <td>${product.price}</td>
            <td>${product.stock}</td>
            <td>${product.threshold}</td>
        </tr>
        `;

        table.innerHTML += row;

    });

}