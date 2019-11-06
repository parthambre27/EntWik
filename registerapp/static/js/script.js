(function($) {

    // DOM Ready Function
    $(function() {
        Carousel.init();
    });

    Carousel = {
        init: function() {
            // Common jQuery Elements
            this.$container = $('.carousel');
            this.$triggerNext = this.$container.find('.js-carousel-nav_next');
            this.$triggerPrev = this.$container.find('.js-carousel-nav_prev');
            this.$carousel = $('.carousel-list');
            this.$carouselListItem = this.$carousel.find('li');
            this.$carouselListItemFirst = this.$carousel.find('li:first');
            this.$carouselListItemLast = this.$carousel.find('li:last');
            this.$carouselItem = $('.carousel-item');
            this.$selectedItem = this.$carousel.find('.carousel-item_isSelected');

            // Common Markers/Placeholders
            this.marker = this.$selectedItem.index();
            this.paddedMarker = this.$selectedItem.index() + 1;
            this.viewportWidth = this.$carouselItem.width();
            this.carouselItemLength = this.$carouselItem.length;
            this.theEnd = this.carouselItemLength - 1;

            // Initiate Functions
            this.bulletNav();
            this.bindEvents();
            //this.autoPlay();
        },

        bindEvents: function() {
            var self = this;
            var $triggerBullet = this.$container.find('.js-carousel-bulletNav-control');
            //var indexBullet = $triggerBullet.index();

            this.$triggerNext.on('click', function(e) {
                e.preventDefault();
                self.nextSlide();
            });

            this.$triggerPrev.on('click', function(e) {
                e.preventDefault();
                self.prevSlide();
            });

            $triggerBullet.on('click', function(e, i) {
                var $this = $(this);
                var i = $this.index();

                e.preventDefault();
                self.bulletNavControl(i);
            });
        },

        //Return the value to slide container by
        slideBy: function() {
            var slideBy = (this.viewportWidth * -this.marker) + 'px';

            return slideBy;
        },

        updateMarkerNext: function() {
            var $currentActive = this.$carousel.find('.carousel-item_isSelected');

            $currentActive.removeClass('carousel-item_isSelected');
            $currentActive.next().addClass('carousel-item_isSelected');
        },

        updateMarkerPrev: function() {
            var $currentActive = this.$carousel.find('.carousel-item_isSelected');

            $currentActive.removeClass('carousel-item_isSelected');
            $currentActive.prev().addClass('carousel-item_isSelected');
        },

        updateMarkerToFirst: function() {
            this.$carouselListItemLast.removeClass('carousel-item_isSelected');
            this.$carouselListItemFirst.addClass('carousel-item_isSelected');
        },

        updateMarkerToLast: function() {
            this.$carouselListItemFirst.removeClass('carousel-item_isSelected');
            this.$carouselListItemLast.addClass('carousel-item_isSelected');
        },

        incrementSlide: function() {
            if (this.marker < this.carouselItemLength) {
                this.marker++;
            } else {
                this.marker = 1;
            }
        },

        decrementSlide: function() {
            if (this.marker == 0 ) {
                this.marker = this.theEnd;
            } else {
                this.marker--;
            }
        },

        // Go to next slide
        nextSlide: function() {
            this.incrementSlide();

            if (this.marker < this.carouselItemLength) {
                this.updateMarkerNext();
                this.$carousel.css('margin-left', this.slideBy());
            } else {
                this.updateMarkerToFirst();
                this.$carousel.css('margin-left', 0);
            }
        },

        // Go to previous slide
        prevSlide: function() {
            this.decrementSlide();

            if (this.marker == this.theEnd) {
                this.updateMarkerToLast();
                this.$carousel.css('margin-left', this.slideBy());
            } else {
                this.updateMarkerPrev();
                this.$carousel.css('margin-left', this.slideBy());
            }
            
        },

        bulletNav: function() {
            var $bulletNav = $('.carousel-bulletNav');

            for(i = 0; i < this.carouselItemLength; i++) {
                $bulletNav.append('<li class="carousel-bulletNav-control js-carousel-bulletNav-control"><a></a></li>');
            }
        },

        updateMarkerBullet: function(index) {
            var $currentActive = this.$carousel.find('.carousel-item_isSelected');

            $currentActive.removeClass('carousel-item_isSelected');
            this.$carouselItem.eq(index).addClass('carousel-item_isSelected');
        },

        bulletNavControl: function(index) {
            var slideByBullet = (this.viewportWidth * -index) + 'px';

            this.$carousel.css('margin-left', slideByBullet);
            this.updateMarkerBullet(index);
            this.marker = index;
        }
    }
    
    
     /*   playA: function() {
            if (this.marker <= this.carouselItemLength) {
                this.nextSlide();
            } else {       
                this.$carousel.css('margin-left', 0);
                this.updateMarkerToLast();
            }
        };

        autoPlay: function(){
            var self = this;
            var run = setInterval(this.playA.bind(this), 3000);

            $('.carousel-viewport').mouseenter(function() {
                clearInterval(run);
            }).mouseleave(function(){
                run = setInterval(self.playA.bind(self), 3000);
            });
        };*/
		
}(jQuery));

(function() {
  
  var Menu = (function() {
    var burger = document.querySelector('.burger');
    var menu = document.querySelector('.menu');
    var menuList = document.querySelector('.menu__list');
    var brand = document.querySelector('.menu__brand');
    var menuItems = document.querySelectorAll('.menu__item');
    
    var active = false;
    
    var toggleMenu = function() {
      if (!active) {
        menu.classList.add('menu--active');
        menuList.classList.add('menu__list--active');
        brand.classList.add('menu__brand--active');
        burger.classList.add('burger--close');
        for (var i = 0, ii = menuItems.length; i < ii; i++) {
          menuItems[i].classList.add('menu__item--active');
        }
        
        active = true;
      } else {
        menu.classList.remove('menu--active');
        menuList.classList.remove('menu__list--active');
        brand.classList.remove('menu__brand--active');
        burger.classList.remove('burger--close');
        for (var i = 0, ii = menuItems.length; i < ii; i++) {
          menuItems[i].classList.remove('menu__item--active');
        }
        
        active = false;
      }
    };
    
    var bindActions = function() {
      burger.addEventListener('click', toggleMenu, false);
    };
	
	var bindActionsM = function() {
      for (var i = 0, ii = menuItems.length; i < ii; i++) {
          menuItems[i].addEventListener('click', toggleMenu, false);
        }
    };
    
    var init = function() {
      bindActions();
	  bindActionsM();
    };
    
    return {
      init: init
    };
    
  }());
  
  Menu.init();
  
}());

