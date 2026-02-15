document.querySelector(".btn-primary").addEventListener("click", () => {
    alert("Thank you for your interest! Our agent will contact you shortly.");
});
document.querySelectorAll("nav a").forEach(link => {
    link.addEventListener("mouseenter", () => {
        link.style.opacity = "0.7";
    });

    link.addEventListener("mouseleave", () => {
        link.style.opacity = "1";
    });
});
const filterSelect = document.querySelector(".section-header select");
const cards = document.querySelectorAll(".property-card");

filterSelect.addEventListener("change", () => {
    const value = filterSelect.value;

    cards.forEach(card => {
        const developer = card.getAttribute("data-developer");

        if (value === "Search for developer..." || developer === value) {
            card.style.display = "block";
        } else {
            card.style.display = "none";
        }
    });
});