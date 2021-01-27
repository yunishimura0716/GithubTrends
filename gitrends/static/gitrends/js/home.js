let showmoreRepo = $('.showmore_repo');
let showmoreRepoOpen = parseInt(showmoreRepo.height())
let showmoreRepoClose = parseInt(showmoreRepo.height() * 0.2)

// initial value
showmoreRepo.css('height', showmoreRepoClose + 'px')

$('.repo_toggle a').click(function () {
    let thisBtn = $(this);
    showmoreTop = showmoreRepo.offset().top

    if ($(this).hasClass('open_repo')) {
        thisBtn
            .removeClass('open_repo')
            .addClass('close_repo')
            .parent().addClass('close_area');
        showmoreRepo
            .css('height', showmoreRepoOpen + 'px');
    } else if ($(this).hasClass('close_repo')) {
        thisBtn
            .removeClass('close_repo')
            .addClass('open_repo')
            .parent().removeClass('close_area');
        showmoreRepo
            .css('height', showmoreRepoClose + 'px')

    }
});