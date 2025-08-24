// Enhanced JavaScript for interactive features
document.addEventListener('DOMContentLoaded', () => {
  
  // Enhanced button animations
  const buttons = document.querySelectorAll('.btn-bounce, .card-hover');
  buttons.forEach(btn => {
    btn.addEventListener('mouseenter', () => {
      btn.style.transform = 'translateY(-5px) scale(1.05)';
      btn.style.transition = 'all 0.3s cubic-bezier(0.4, 0, 0.2, 1)';
    });
    
    btn.addEventListener('mouseleave', () => {
      btn.style.transform = 'translateY(0) scale(1)';
    });
  });

  // Parallax effect for floating elements
  const floatingElements = document.querySelectorAll('.animate-float');
  window.addEventListener('scroll', () => {
    const scrolled = window.pageYOffset;
    floatingElements.forEach((el, index) => {
      const rate = scrolled * -0.5 * (index + 1);
      el.style.transform = `translateY(${rate}px)`;
    });
  });

  // Form validation with animations
  const forms = document.querySelectorAll('form');
  forms.forEach(form => {
    form.addEventListener('submit', (e) => {
      const inputs = form.querySelectorAll('input[required], select[required], textarea[required]');
      let isValid = true;
      
      inputs.forEach(input => {
        if (!input.value.trim()) {
          input.style.borderColor = '#ef4444';
          input.style.animation = 'wiggle 0.5s ease-in-out';
          isValid = false;
          
          setTimeout(() => {
            input.style.animation = '';
            input.style.borderColor = '';
          }, 500);
        }
      });
      
      if (!isValid) {
        e.preventDefault();
      }
    });
  });

  // Smooth reveal animations on scroll
  const observeElements = document.querySelectorAll('.animate-fade-in, .animate-slide-in, .animate-scale-in');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
      }
    });
  }, { threshold: 0.1 });
  
  observeElements.forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'all 0.6s ease-out';
    observer.observe(el);
  });

  // Add sparkle effect to rainbow buttons
  const rainbowBtns = document.querySelectorAll('.btn-rainbow');
  rainbowBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      const sparkle = document.createElement('div');
      sparkle.innerHTML = '✨';
      sparkle.style.position = 'absolute';
      sparkle.style.left = e.clientX + 'px';
      sparkle.style.top = e.clientY + 'px';
      sparkle.style.pointerEvents = 'none';
      sparkle.style.animation = 'sparkle 1s ease-out forwards';
      document.body.appendChild(sparkle);
      
      setTimeout(() => sparkle.remove(), 1000);
    });
  });
});

// CSS animation for sparkle effect
const style = document.createElement('style');
style.textContent = `
  @keyframes sparkle {
    0% { transform: scale(0) rotate(0deg); opacity: 1; }
    100% { transform: scale(2) rotate(180deg); opacity: 0; }
  }
`;
document.head.appendChild(style);
