// animation for subject options lijnearly display when clicked on button
const launcher = document.getElementById("launcher");
const buttons = document.querySelectorAll(".subjectbutton");
let opened = false
launcher.addEventListener("click", () => {
    opened = !opened;
    buttons.forEach((btn, i) => {
        setTimeout(() => {
            if (opened) {
                btn.classList.add("show");
            } else {
                btn.classList.remove("show");
            }
        }, i * 100); // stagger animation by 100ms per button
    });
});

//animation for infiite ribbon text display
document.addEventListener('DOMContentLoaded', function() {
    const ribbonTrack = document.getElementById('ribbonTrack');
    
    // Text items with consistent styling
    const items = [
        { text: 'Creative' },
        { text: 'Fast' },
        { text: 'Innovative' },
        { text: 'Beautiful' },
        { text: 'Dynamic' },
        { text: 'Customizable' },
        { text: 'Global' },
        { text: 'Precise' },
        { text: 'Powerful' },
        { text: 'Premium' }
    ];
    
    // Function to create ribbon items
    function createRibbonItems() {
        // Add items twice for seamless looping
        for (let i = 0; i < 2; i++) {
            items.forEach(item => {
                const element = document.createElement('span');
                element.className = 'ribbon-item';
                element.textContent = item.text;
                ribbonTrack.appendChild(element);
            });
        }
    }
    
    // Initialize the ribbon
    createRibbonItems();
    
    // Pause animation on hover
    ribbonTrack.addEventListener('mouseenter', () => {
        ribbonTrack.style.animationPlayState = 'paused';
    });
    
    ribbonTrack.addEventListener('mouseleave', () => {
        ribbonTrack.style.animationPlayState = 'running';
    });
});