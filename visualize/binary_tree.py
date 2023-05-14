from datastructures.trees.binarytree import BinaryTree
import pygame

# Initialize pygame.
pygame.init()

# Create a window
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Binary Tree Traversal")

colors = {
    'green': (0, 150, 0),
    'red': (255, 255, 255),
    'black': (80, 80, 80),
    'gray': (240, 240, 240)
}


def draw_buttons(win, x, y, z):
    pygame.draw.rect(win, x, y, z)
    btn_font = pygame.font.Font(None, 24)
    text = btn_font.render("Preorder", True, colors.get('black'))
    rect = text.get_rect(center=(x, y))

    win.blit(text, rect)
    pygame.display.update()


def draw_tree(win, tree, node, x, y, z):
    # Draw the root.
    pygame.draw.circle(win, colors.get('green'), (x, y), 20)
    font = pygame.font.Font(None, 24)
    text = font.render(str(node.value), True, (255, 255, 255))
    text_rect = text.get_rect(center=(x, y))

    # Blit the text on the window.
    win.blit(text, text_rect)
    pygame.display.update()

    # Draw the children
    if node.left is not None:
        pygame.draw.line(win, colors.get('gray'), (x, y), (x - z, y + 80))
        draw_tree(win, tree, node.left, x - z, y + 80, z // 2)
    if node.right is not None:
        pygame.draw.line(win, colors.get('gray'), (x, y), (x + z, y + 80))
        draw_tree(win, tree, node.right, x + z, y + 80, z // 2)


def traverse_tree(win, tree, node, x, y, dx, order):
    if node is None:
        return

    if order == 'pre':
        highlight_node(win, x, y, node.value)
    traverse_tree(win, tree, node.left, x - dx, y + 80, dx // 2, order)

    if order == 'in':
        highlight_node(win, x, y, node.value)
    traverse_tree(win, tree, node.right, x + dx, y + 80, dx // 2, order)

    if order == 'post':
        highlight_node(win, x, y, node.value)


def highlight_node(win, x, y, value):
    pygame.draw.circle(win, (255, 0, 0), (x, y), 20)

    font = pygame.font.Font(None, 24)
    text = font.render(str(value), True, colors.get('red'))
    text_rect = text.get_rect(center=(x, y))

    win.blit(text, text_rect)
    pygame.display.update()
    pygame.time.delay(600)


# Main code
root = BinaryTree()

# Insert children.
root.insert(10)
root.insert(8)
root.insert(15)
root.insert(2)
root.insert(9)
root.insert(22)
root.insert(15)

traversal_finished = False
clock = pygame.time.Clock()

while not traversal_finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Draw tree
    window.fill((colors.get('black')))
    draw_buttons(window)
    draw_tree(window, root, root.root, 400, 200, 200)

    pygame.display.update()

    # Traverse tree
    # traverse_tree(window, root, root.root, 400, 200, 200, 'in')
    # traversal_finished = True
    clock.tick(1)

pygame.display.quit()
pygame.quit()
