// Mock Data
const products = [
    {
        id: 1,
        name: "NVIDIA RTX 5090 Ti",
        category: "Components",
        price: 1999.99,
        image: "https://images.unsplash.com/photo-1591488320449-011701bb6704?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Z3JhcGhpY3MlMjBjYXJkfGVufDB8fDB8fHww",
        description: "The absolute pinnacle of graphical processing power."
    },
    {
        id: 2,
        name: "Oculus Pro X",
        category: "VR/AR",
        price: 1499.00,
        image: "https://images.unsplash.com/photo-1593508512255-86ab42a8e620?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OXx8dnIlMjBoZWFkc2V0fGVufDB8fDB8fHww",
        description: "Next-gen immersion with haptic feedback integration."
    },
    {
        id: 3,
        name: "Quantum Core i9-15900K",
        category: "Components",
        price: 799.99,
        image: "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Y3B1fGVufDB8fDB8fHww",
        description: "Unleash multithreaded dominance on your workload."
    },
    {
        id: 4,
        name: "Cyber-Deck Mechanical Keyboard",
        category: "Peripherals",
        price: 249.50,
        image: "https://images.unsplash.com/photo-1595225476474-87563907a212?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8bWVjaGFuaWNhbCUyMGtleWJvYXJkfGVufDB8fDB8fHww",
        description: "Custom switches with programmable OLED displays."
    },
    {
        id: 5,
        name: "Holo-Display 8K",
        category: "Monitors",
        price: 3499.99,
        image: "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Z2FtaW5nJTIwbW9uaXRvcnxlbnwwfHwwfHx8MA%3D%3D",
        description: "Borderless 8K resolution with holographic projection."
    },
    {
        id: 6,
        name: "Neural Link Interface",
        category: "Experimental",
        price: 5000.00,
        image: "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fHRlY2hub2xvZ3l8ZW58MHx8MHx8fDA%3D",
        description: "Direct brain-computer interface for zero latency gaming."
    }
];

// State
let cart = [];

// DOM Elements
const productsGrid = document.getElementById('products-grid');
const searchInput = document.getElementById('search-input');
const cartBtn = document.getElementById('cart-btn');
const closeCartBtn = document.getElementById('close-cart');
const cartSidebar = document.getElementById('cart-sidebar');
const overlay = document.getElementById('overlay');
const cartItemsContainer = document.getElementById('cart-items');
const cartCountElement = document.getElementById('cart-count');
const cartTotalElement = document.getElementById('cart-total');

// Initialization
document.addEventListener('DOMContentLoaded', () => {
    renderProducts(products);
    updateCartUI();
});

// Render Products
function renderProducts(items) {
    productsGrid.innerHTML = '';

    if (items.length === 0) {
        productsGrid.innerHTML = '<p class="no-results">No products found in this sector.</p>';
        return;
    }

    items.forEach(product => {
        const productCard = document.createElement('div');
        productCard.className = 'product-card';
        productCard.innerHTML = `
            <div class="product-image-container">
                <img src="${product.image}" alt="${product.name}" class="product-image">
            </div>
            <div class="product-info">
                <span class="product-category">${product.category}</span>
                <h3 class="product-title">${product.name}</h3>
                <div class="product-price">$${product.price.toFixed(2)}</div>
                <button class="add-to-cart-btn" onclick="addToCart(${product.id})">
                    Add to Cart
                </button>
            </div>
        `;
        productsGrid.appendChild(productCard);
    });
}

// Search Functionality
searchInput.addEventListener('input', (e) => {
    const query = e.target.value.toLowerCase();
    const filteredProducts = products.filter(product =>
        product.name.toLowerCase().includes(query) ||
        product.category.toLowerCase().includes(query)
    );
    renderProducts(filteredProducts);
});

// Cart Logic
window.addToCart = (productId) => {
    const product = products.find(p => p.id === productId);
    if (product) {
        cart.push(product);
        updateCartUI();
        openCart();
    }
};

window.removeFromCart = (index) => {
    cart.splice(index, 1);
    updateCartUI();
};

function updateCartUI() {
    // Update Count
    cartCountElement.textContent = cart.length;

    // Update Total
    const total = cart.reduce((sum, item) => sum + item.price, 0);
    cartTotalElement.textContent = '$' + total.toFixed(2);

    // Render Items
    cartItemsContainer.innerHTML = '';

    if (cart.length === 0) {
        cartItemsContainer.innerHTML = '<div class="empty-cart-msg">Your cart is empty.</div>';
        return;
    }

    cart.forEach((item, index) => {
        const cartItem = document.createElement('div');
        cartItem.className = 'cart-item';
        cartItem.innerHTML = `
            <img src="${item.image}" alt="${item.name}" class="cart-item-img">
            <div class="cart-item-details">
                <h4 class="cart-item-title">${item.name}</h4>
                <div class="cart-item-price">$${item.price.toFixed(2)}</div>
                <button class="cart-item-remove" onclick="removeFromCart(${index})">Remove</button>
            </div>
        `;
        cartItemsContainer.appendChild(cartItem);
    });
}

// Sidebar Toggles
function openCart() {
    cartSidebar.classList.add('open');
    overlay.classList.add('active');
}

function closeCart() {
    cartSidebar.classList.remove('open');
    overlay.classList.remove('active');
}

cartBtn.addEventListener('click', openCart);
closeCartBtn.addEventListener('click', closeCart);
overlay.addEventListener('click', closeCart);
