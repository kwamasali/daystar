// Navigation bar

const menu = document.querySelector('#mobile-menu');
const menuLinks = document.querySelector('.navbar__menu');
const navbar__logo =document.querySelector('#navbar__logo')


// Display mobile menu
const mobileMenu = () => {
    menu.classList.toggle('is-active');
    menuLinks.classList.toggle('active');
  };
  
  menu.addEventListener('click', mobileMenu);

// Show active menu when scrolling
const highlightMenu = () => {
    const elem = document.querySelector('.highlight')
    const homePage = document.querySelector('/daystar-app/home.html')
    const babiesPage = document.querySelector('/daystar-app/babies.html')
    const sittersPage = document.querySelector('/daystar-app/sitters.html')
    const paymentPage = document.querySelector('/daystar-app/payment.html')
    const dollShop = document.querySelector('/daystar-app/dolls-shop.html')

    let scrollPos = window.scrollY
    console.log(scrollPos);

    // adds the highlight class to my menu items
    if (window.innerWidth > 960 && scrollPos < 600) {
        homePage.classList.add('highlight');
        babiesPage.classList.remove('highlight');
        return;
      } else if (window.innerWidth > 960 && scrollPos < 1400) {
        homePage.classList.add('highlight');
        babiesPage.classList.remove('highlight');
        sittersPage.classList.remove('highlight');
        paymentPage.classList.remove('highlight');
        dollShop.classList.remove('highlight');
        return;
      } else if (window.innerWidth > 960 && scrollPos < 2345) {
        sittersPage.classList.add('highlight');
        paymentPage.classList.add('highlight');
        dollShop.classList.remove('highlight');
        return;
      }
    
      if ((elem && window.innerWIdth < 960 && scrollPos < 600) || elem) {
        elem.classList.remove('highlight');
      }
    };
    
    window.addEventListener('scroll', highlightMenu);
    window.addEventListener('click', highlightMenu);

 //  Close mobile Menu when clicking on a menu item
const hideMobileMenu = () => {
    const menuBars = document.querySelector('.is-active');
    if (window.innerWidth <= 768 && menuBars) {
      menu.classList.toggle('is-active');
      menuLinks.classList.remove('active');
    }
  };
  
  menuLinks.addEventListener('click', hideMobileMenu);
  navLogo.addEventListener('click', hideMobileMenu);