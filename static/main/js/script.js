document.addEventListener('DOMContentLoaded', function () {
   
    const menuButton = document.getElementById('menu-toggle');
    const sidebar = document.getElementById('sidebar');

   
    if (!menuButton || !sidebar) {
        console.error('Error: Could not find menuButton or sidebar elements.');
        return;
    }

    menuButton.addEventListener('click', function () {
        console.log('Menu button clicked!'); 
        sidebar.classList.toggle('visible'); 
    });

    console.log('JavaScript loaded successfully!');
});
