document.addEventListener('DOMContentLoaded', function() {
  const copyButtons = document.querySelectorAll('.copy-btn');
  
  copyButtons.forEach(button => {
    button.addEventListener('click', function() {
      const textToCopy = this.getAttribute('data-copy');
      
      navigator.clipboard.writeText(textToCopy).then(() => {
        const originalText = this.textContent;
        this.textContent = '✓ 已複製！';
        this.style.backgroundColor = '#28a745';
        
        setTimeout(() => {
          this.textContent = originalText;
          this.style.backgroundColor = '#159957';
        }, 2000);
      }).catch(err => {
        alert('複製失敗，請手動複製');
      });
    });
  });
});
