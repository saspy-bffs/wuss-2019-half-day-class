# This modules contains definitions used in Example Files


def print_with_title(
        output: str,
        title: str = '',
        linebreaks_before: int = 2,
        linebreaks_after: int = 2,
        put_stars_after: bool = True,
) -> None:
    """
    Print linebreak-padded output with a title and optional line of 80 stars
    afterward
    """
    print(
        '\n' * linebreaks_before + title + '\n' * 2,
        output,
        '\n' * linebreaks_after,
        sep='',
    )
    if put_stars_after:
        print('*' * 80)


if __name__ == '__main__':
    print_with_title('This module is working as expected!')
