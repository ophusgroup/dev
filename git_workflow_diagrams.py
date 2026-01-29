import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# Colors
remote_color = '#e3f2fd'
local_color = '#fff3e0'
upstream_color = '#bbdefb'
origin_color = '#c8e6c9'
clone_color = '#ffe0b2'
will_color = '#f3e5f5'  # light purple for Case 1


def case1_prototyping():
    """Case 1: Prototyping on your fork - PR goes to colleague's fork"""
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.axis('off')

    # Remote box (GitHub)
    remote_box = FancyBboxPatch((0.3, 5.5), 13.4, 4.2,
                                 boxstyle="round,pad=0.05,rounding_size=0.3",
                                 facecolor=remote_color, edgecolor='#1976d2', linewidth=3)
    ax.add_patch(remote_box)
    ax.text(7, 9.4, 'Remote (GitHub)', ha='center', va='center', fontsize=22, fontweight='bold', color='#1976d2')

    # Local box (Will's Computer) - LEFT
    will_local_box = FancyBboxPatch((0.5, 0.3), 5.5, 3.2,
                                boxstyle="round,pad=0.05,rounding_size=0.3",
                                facecolor=will_color, edgecolor='#7b1fa2', linewidth=3)
    ax.add_patch(will_local_box)
    ax.text(3.25, 3.2, "Local (Will's Computer)", ha='center', va='center', fontsize=18, fontweight='bold', color='#7b1fa2')

    # Will's clone box
    will_clone_box = FancyBboxPatch((0.8, 0.6), 4.9, 2.0,
                                boxstyle="round,pad=0.05,rounding_size=0.2",
                                facecolor=clone_color, edgecolor='#ef6c00', linewidth=2)
    ax.add_patch(will_clone_box)
    ax.text(3.25, 2.0, '~/repos/quantem', ha='center', va='center', fontsize=14, fontweight='bold')
    ax.text(3.25, 1.5, 'git checkout -b align', ha='center', va='center', fontsize=9, color='#666', style='italic')
    ax.text(3.25, 1.1, 'git add · git commit · git push', ha='center', va='center', fontsize=9, color='#666', style='italic')

    # Local box (Colin's Computer) - RIGHT
    colin_local_box = FancyBboxPatch((8, 0.3), 5.5, 3.2,
                                boxstyle="round,pad=0.05,rounding_size=0.3",
                                facecolor=local_color, edgecolor='#e65100', linewidth=3)
    ax.add_patch(colin_local_box)
    ax.text(10.75, 3.2, "Local (Colin's Computer)", ha='center', va='center', fontsize=18, fontweight='bold', color='#e65100')

    # Colin's clone box
    colin_clone_box = FancyBboxPatch((8.3, 0.6), 4.9, 2.0,
                                boxstyle="round,pad=0.05,rounding_size=0.2",
                                facecolor=clone_color, edgecolor='#ef6c00', linewidth=2)
    ax.add_patch(colin_clone_box)
    ax.text(10.75, 2.0, '~/repos/quantem', ha='center', va='center', fontsize=14, fontweight='bold')
    ax.text(10.75, 1.5, 'git checkout -b align-subpixel', ha='center', va='center', fontsize=9, color='#666', style='italic')
    ax.text(10.75, 1.1, 'git add · git commit · git push', ha='center', va='center', fontsize=9, color='#666', style='italic')

    # Upstream box (org repo - faded/background)
    upstream_box = FancyBboxPatch((0.6, 5.9), 3.4, 2.8,
                                   boxstyle="round,pad=0.05,rounding_size=0.2",
                                   facecolor='#f5f5f5', edgecolor='#9e9e9e', linewidth=2, linestyle='dashed')
    ax.add_patch(upstream_box)
    ax.text(2.3, 8.0, '"upstream"', ha='center', va='center', fontsize=16, fontweight='bold', color='#9e9e9e')
    ax.text(2.3, 7.3, 'electronmicroscopy/', ha='center', va='center', fontsize=12, style='italic', color='#9e9e9e')
    ax.text(2.3, 6.75, 'quantem', ha='center', va='center', fontsize=12, style='italic', color='#9e9e9e')

    # Will's fork box
    will_box = FancyBboxPatch((4.3, 5.9), 3.4, 2.8,
                                boxstyle="round,pad=0.05,rounding_size=0.2",
                                facecolor=will_color, edgecolor='#7b1fa2', linewidth=2)
    ax.add_patch(will_box)
    ax.text(6, 8.0, '"will"', ha='center', va='center', fontsize=16, fontweight='bold')
    ax.text(6, 7.3, 'wwmills/', ha='center', va='center', fontsize=12, style='italic')
    ax.text(6, 6.75, 'quantem:align', ha='center', va='center', fontsize=12, style='italic', fontweight='bold')

    # Origin box (Colin's fork)
    origin_box = FancyBboxPatch((10, 5.9), 3.4, 2.8,
                                 boxstyle="round,pad=0.05,rounding_size=0.2",
                                 facecolor=origin_color, edgecolor='#388e3c', linewidth=2)
    ax.add_patch(origin_box)
    ax.text(11.7, 8.0, '"origin"', ha='center', va='center', fontsize=16, fontweight='bold')
    ax.text(11.7, 7.3, 'cophus/', ha='center', va='center', fontsize=12, style='italic')
    ax.text(11.7, 6.75, 'quantem:align-subpixel', ha='center', va='center', fontsize=12, style='italic', fontweight='bold')

    # Step 1: Will pushes to his fork
    ax.annotate('', xy=(5.5, 5.8), xytext=(3.5, 3.6),
                arrowprops=dict(arrowstyle='->', color='#7b1fa2', lw=3))
    ax.text(2.2, 4.6, 'git push', ha='center', va='center', fontsize=12, color='#7b1fa2', fontweight='bold')
    circle1 = plt.Circle((2.2, 5.0), 0.25, color='#7b1fa2', zorder=5)
    ax.add_patch(circle1)
    ax.text(2.2, 5.0, '1', ha='center', va='center', fontsize=14, color='white', fontweight='bold', zorder=6)

    # Step 2: Colin fetches from Will - from will box down to Colin's local
    ax.annotate('', xy=(10.0, 3.6), xytext=(6.5, 5.8),
                arrowprops=dict(arrowstyle='->', color='#d32f2f', lw=3))
    ax.text(9.5, 4.9, 'git fetch will', ha='center', va='center', fontsize=13, color='#d32f2f', fontweight='bold')
    circle2 = plt.Circle((9.5, 5.3), 0.25, color='#d32f2f', zorder=5)
    ax.add_patch(circle2)
    ax.text(9.5, 5.3, '2', ha='center', va='center', fontsize=14, color='white', fontweight='bold', zorder=6)

    # Step 3: Colin pushes to his origin
    ax.annotate('', xy=(11.7, 5.8), xytext=(11.0, 3.6),
                arrowprops=dict(arrowstyle='->', color='#1976d2', lw=3))
    ax.text(12.5, 4.6, 'git push', ha='center', va='center', fontsize=14, color='#1976d2', fontweight='bold')
    circle3 = plt.Circle((12.5, 5.0), 0.25, color='#1976d2', zorder=5)
    ax.add_patch(circle3)
    ax.text(12.5, 5.0, '3', ha='center', va='center', fontsize=14, color='white', fontweight='bold', zorder=6)

    # Step 4: PR (Colin's origin -> Will's fork) - dashed
    ax.annotate('', xy=(7.8, 7.3), xytext=(9.9, 7.3),
                arrowprops=dict(arrowstyle='->', color='#7b1fa2', lw=3, linestyle='dashed'))
    ax.text(8.85, 6.9, 'PR to will', ha='center', va='center', fontsize=16, color='#7b1fa2', fontweight='bold')
    circle4 = plt.Circle((8.85, 7.65), 0.25, color='#7b1fa2', zorder=5)
    ax.add_patch(circle4)
    ax.text(8.85, 7.65, '4', ha='center', va='center', fontsize=14, color='white', fontweight='bold', zorder=6)

    plt.tight_layout(pad=0.1)
    plt.savefig('img/git_workflow_case1.png', dpi=150, bbox_inches='tight', facecolor='white', pad_inches=0.1)
    plt.close()
    print("Saved img/git_workflow_case1.png")


def case3_quick_fixes():
    """Case 3: Quick fixes - PR goes directly to upstream/dev"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.set_aspect('equal')
    ax.axis('off')

    # Remote box (GitHub)
    remote_box = FancyBboxPatch((0.3, 4), 11.4, 3.7,
                                 boxstyle="round,pad=0.05,rounding_size=0.3",
                                 facecolor=remote_color, edgecolor='#1976d2', linewidth=3)
    ax.add_patch(remote_box)
    ax.text(6, 7.4, 'Remote (GitHub)', ha='center', va='center', fontsize=22, fontweight='bold', color='#1976d2')

    # Local box (Your Computer)
    local_box = FancyBboxPatch((3, 0.3), 6, 2.8,
                                boxstyle="round,pad=0.05,rounding_size=0.3",
                                facecolor=local_color, edgecolor='#e65100', linewidth=3)
    ax.add_patch(local_box)
    ax.text(6, 2.85, 'Local (Your Computer)', ha='center', va='center', fontsize=22, fontweight='bold', color='#e65100')

    # Upstream box
    upstream_box = FancyBboxPatch((0.8, 4.4), 4.4, 2.4,
                                   boxstyle="round,pad=0.05,rounding_size=0.2",
                                   facecolor=upstream_color, edgecolor='#1565c0', linewidth=2)
    ax.add_patch(upstream_box)
    ax.text(3, 6.2, '"upstream"', ha='center', va='center', fontsize=20, fontweight='bold')
    ax.text(3, 5.5, 'electronmicroscopy/', ha='center', va='center', fontsize=14, style='italic')
    ax.text(3, 4.95, 'quantem:dev', ha='center', va='center', fontsize=14, style='italic', fontweight='bold')

    # Origin box (fork) - Bob's fork
    origin_box = FancyBboxPatch((6.8, 4.4), 4.4, 2.4,
                                 boxstyle="round,pad=0.05,rounding_size=0.2",
                                 facecolor=origin_color, edgecolor='#388e3c', linewidth=2)
    ax.add_patch(origin_box)
    ax.text(9, 6.2, '"origin"', ha='center', va='center', fontsize=20, fontweight='bold')
    ax.text(9, 5.5, '<your-username>/', ha='center', va='center', fontsize=14, style='italic')
    ax.text(9, 4.95, 'quantem:fix-readme-typo', ha='center', va='center', fontsize=12, style='italic', fontweight='bold')

    # Clone box
    clone_box = FancyBboxPatch((3.5, 0.6), 5, 1.8,
                                boxstyle="round,pad=0.05,rounding_size=0.2",
                                facecolor=clone_color, edgecolor='#ef6c00', linewidth=2)
    ax.add_patch(clone_box)
    ax.text(6, 1.9, '~/repos/quantem', ha='center', va='center', fontsize=18, fontweight='bold')
    ax.text(6, 1.4, 'git checkout -b fix-readme-typo', ha='center', va='center', fontsize=10, color='#666', style='italic')
    ax.text(6, 1.0, 'git add · git commit · git push', ha='center', va='center', fontsize=10, color='#666', style='italic')

    # Step 1: git checkout dev + git pull upstream dev
    ax.annotate('', xy=(4.2, 3.2), xytext=(3.2, 4.3),
                arrowprops=dict(arrowstyle='->', color='#d32f2f', lw=3))
    ax.text(2.4, 3.75, 'git checkout dev', ha='center', va='center', fontsize=12, color='#d32f2f', fontweight='bold')
    ax.text(2.4, 3.4, 'git pull upstream dev', ha='center', va='center', fontsize=12, color='#d32f2f', fontweight='bold')
    # Circle with number 1
    circle1 = plt.Circle((2.4, 4.1), 0.25, color='#d32f2f', zorder=5)
    ax.add_patch(circle1)
    ax.text(2.4, 4.1, '1', ha='center', va='center', fontsize=14, color='white', fontweight='bold', zorder=6)

    # Step 2: git push
    ax.annotate('', xy=(8.8, 4.3), xytext=(7.6, 3.2),
                arrowprops=dict(arrowstyle='->', color='#1976d2', lw=3))
    ax.text(9.6, 3.6, 'git push', ha='center', va='center', fontsize=16, color='#1976d2', fontweight='bold')
    # Circle with number 2
    circle2 = plt.Circle((9.6, 4.0), 0.25, color='#1976d2', zorder=5)
    ax.add_patch(circle2)
    ax.text(9.6, 4.0, '2', ha='center', va='center', fontsize=14, color='white', fontweight='bold', zorder=6)

    # Step 3: PR (origin -> upstream:dev)
    ax.annotate('', xy=(5.3, 5.5), xytext=(6.7, 5.5),
                arrowprops=dict(arrowstyle='->', color='#7b1fa2', lw=3, linestyle='dashed'))
    ax.text(6, 5.15, 'PR to dev', ha='center', va='center', fontsize=18, color='#7b1fa2', fontweight='bold')
    # Circle with number 3
    circle3 = plt.Circle((6, 5.85), 0.25, color='#7b1fa2', zorder=5)
    ax.add_patch(circle3)
    ax.text(6, 5.85, '3', ha='center', va='center', fontsize=14, color='white', fontweight='bold', zorder=6)

    plt.tight_layout(pad=0.1)
    plt.savefig('img/git_workflow_case3.png', dpi=150, bbox_inches='tight', facecolor='white', pad_inches=0.1)
    plt.close()
    print("Saved img/git_workflow_case3.png")


def case2_feature_branch():
    """Case 2: Major feature development - PR goes to feature branch (Bob's workflow)"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.set_aspect('equal')
    ax.axis('off')

    # Remote box (GitHub)
    remote_box = FancyBboxPatch((0.3, 4), 11.4, 3.7,
                                 boxstyle="round,pad=0.05,rounding_size=0.3",
                                 facecolor=remote_color, edgecolor='#1976d2', linewidth=3)
    ax.add_patch(remote_box)
    ax.text(6, 7.4, 'Remote (GitHub)', ha='center', va='center', fontsize=22, fontweight='bold', color='#1976d2')

    # Local box (Bob's Computer)
    local_box = FancyBboxPatch((3, 0.3), 6, 2.8,
                                boxstyle="round,pad=0.05,rounding_size=0.3",
                                facecolor=local_color, edgecolor='#e65100', linewidth=3)
    ax.add_patch(local_box)
    ax.text(6, 2.85, "Local (Bob's Computer)", ha='center', va='center', fontsize=22, fontweight='bold', color='#e65100')

    # Upstream box
    upstream_box = FancyBboxPatch((0.8, 4.4), 4.4, 2.4,
                                   boxstyle="round,pad=0.05,rounding_size=0.2",
                                   facecolor=upstream_color, edgecolor='#1565c0', linewidth=2)
    ax.add_patch(upstream_box)
    ax.text(3, 6.2, '"upstream"', ha='center', va='center', fontsize=20, fontweight='bold')
    ax.text(3, 5.5, 'electronmicroscopy/', ha='center', va='center', fontsize=14, style='italic')
    ax.text(3, 4.95, 'quantem:drift-torch', ha='center', va='center', fontsize=14, style='italic', fontweight='bold')

    # Origin box (fork) - Bob's fork
    origin_box = FancyBboxPatch((6.8, 4.4), 4.4, 2.4,
                                 boxstyle="round,pad=0.05,rounding_size=0.2",
                                 facecolor=origin_color, edgecolor='#388e3c', linewidth=2)
    ax.add_patch(origin_box)
    ax.text(9, 6.2, '"origin"', ha='center', va='center', fontsize=20, fontweight='bold')
    ax.text(9, 5.5, 'bobleesj/', ha='center', va='center', fontsize=14, style='italic')
    ax.text(9, 4.95, 'quantem:drift-torch-rigid', ha='center', va='center', fontsize=14, style='italic', fontweight='bold')

    # Clone box
    clone_box = FancyBboxPatch((3.5, 0.6), 5, 1.8,
                                boxstyle="round,pad=0.05,rounding_size=0.2",
                                facecolor=clone_color, edgecolor='#ef6c00', linewidth=2)
    ax.add_patch(clone_box)
    ax.text(6, 1.9, '~/repos/quantem', ha='center', va='center', fontsize=18, fontweight='bold')
    ax.text(6, 1.4, 'git checkout -b drift-torch-rigid', ha='center', va='center', fontsize=10, color='#666', style='italic')
    ax.text(6, 1.0, 'git add · git commit · git push', ha='center', va='center', fontsize=10, color='#666', style='italic')

    # Step 1: git pull upstream drift-torch
    ax.annotate('', xy=(4.2, 3.2), xytext=(3.2, 4.3),
                arrowprops=dict(arrowstyle='->', color='#d32f2f', lw=3))
    ax.text(2.3, 3.6, 'git pull upstream drift-torch', ha='center', va='center', fontsize=14, color='#d32f2f', fontweight='bold')
    circle1 = plt.Circle((2.3, 4.0), 0.25, color='#d32f2f', zorder=5)
    ax.add_patch(circle1)
    ax.text(2.3, 4.0, '1', ha='center', va='center', fontsize=14, color='white', fontweight='bold', zorder=6)

    # Step 2: git push
    ax.annotate('', xy=(8.8, 4.3), xytext=(7.6, 3.2),
                arrowprops=dict(arrowstyle='->', color='#1976d2', lw=3))
    ax.text(9.6, 3.6, 'git push', ha='center', va='center', fontsize=16, color='#1976d2', fontweight='bold')
    circle2 = plt.Circle((9.6, 4.0), 0.25, color='#1976d2', zorder=5)
    ax.add_patch(circle2)
    ax.text(9.6, 4.0, '2', ha='center', va='center', fontsize=14, color='white', fontweight='bold', zorder=6)

    # Step 3: PR (origin -> upstream:drift) - dashed
    ax.annotate('', xy=(5.3, 5.5), xytext=(6.7, 5.5),
                arrowprops=dict(arrowstyle='->', color='#7b1fa2', lw=3, linestyle='dashed'))
    ax.text(6, 5.15, 'PR to drift-torch', ha='center', va='center', fontsize=18, color='#7b1fa2', fontweight='bold')
    circle3 = plt.Circle((6, 5.85), 0.25, color='#7b1fa2', zorder=5)
    ax.add_patch(circle3)
    ax.text(6, 5.85, '3', ha='center', va='center', fontsize=14, color='white', fontweight='bold', zorder=6)

    plt.tight_layout(pad=0.1)
    plt.savefig('img/git_workflow_case2_bob.png', dpi=150, bbox_inches='tight', facecolor='white', pad_inches=0.1)
    plt.close()
    print("Saved img/git_workflow_case2_bob.png")


def case2_will_joins():
    """Case 2: Will joins the feature branch - PR goes to feature branch"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.set_aspect('equal')
    ax.axis('off')

    # Remote box (GitHub)
    remote_box = FancyBboxPatch((0.3, 4), 11.4, 3.7,
                                 boxstyle="round,pad=0.05,rounding_size=0.3",
                                 facecolor=remote_color, edgecolor='#1976d2', linewidth=3)
    ax.add_patch(remote_box)
    ax.text(6, 7.4, 'Remote (GitHub)', ha='center', va='center', fontsize=22, fontweight='bold', color='#1976d2')

    # Local box (Will's Computer)
    local_box = FancyBboxPatch((3, 0.3), 6, 2.8,
                                boxstyle="round,pad=0.05,rounding_size=0.3",
                                facecolor=local_color, edgecolor='#e65100', linewidth=3)
    ax.add_patch(local_box)
    ax.text(6, 2.85, "Local (Will's Computer)", ha='center', va='center', fontsize=22, fontweight='bold', color='#e65100')

    # Upstream box
    upstream_box = FancyBboxPatch((0.8, 4.4), 4.4, 2.4,
                                   boxstyle="round,pad=0.05,rounding_size=0.2",
                                   facecolor=upstream_color, edgecolor='#1565c0', linewidth=2)
    ax.add_patch(upstream_box)
    ax.text(3, 6.2, '"upstream"', ha='center', va='center', fontsize=20, fontweight='bold')
    ax.text(3, 5.5, 'electronmicroscopy/', ha='center', va='center', fontsize=14, style='italic')
    ax.text(3, 4.95, 'quantem:drift-torch', ha='center', va='center', fontsize=14, style='italic', fontweight='bold')

    # Origin box (fork) - Will's fork
    origin_box = FancyBboxPatch((6.8, 4.4), 4.4, 2.4,
                                 boxstyle="round,pad=0.05,rounding_size=0.2",
                                 facecolor=origin_color, edgecolor='#388e3c', linewidth=2)
    ax.add_patch(origin_box)
    ax.text(9, 6.2, '"origin"', ha='center', va='center', fontsize=20, fontweight='bold')
    ax.text(9, 5.5, 'wwmills/', ha='center', va='center', fontsize=14, style='italic')
    ax.text(9, 4.95, 'quantem:drift-torch-test', ha='center', va='center', fontsize=14, style='italic', fontweight='bold')

    # Clone box
    clone_box = FancyBboxPatch((3.5, 0.6), 5, 1.8,
                                boxstyle="round,pad=0.05,rounding_size=0.2",
                                facecolor=clone_color, edgecolor='#ef6c00', linewidth=2)
    ax.add_patch(clone_box)
    ax.text(6, 1.9, '~/repos/quantem', ha='center', va='center', fontsize=18, fontweight='bold')
    ax.text(6, 1.4, 'git checkout -b drift-torch-test', ha='center', va='center', fontsize=10, color='#666', style='italic')
    ax.text(6, 1.0, 'git add · git commit · git push', ha='center', va='center', fontsize=10, color='#666', style='italic')

    # Step 1: git pull upstream drift-torch
    ax.annotate('', xy=(4.2, 3.2), xytext=(3.2, 4.3),
                arrowprops=dict(arrowstyle='->', color='#d32f2f', lw=3))
    ax.text(2.3, 3.6, 'git pull upstream drift-torch', ha='center', va='center', fontsize=14, color='#d32f2f', fontweight='bold')
    circle1 = plt.Circle((2.3, 4.0), 0.25, color='#d32f2f', zorder=5)
    ax.add_patch(circle1)
    ax.text(2.3, 4.0, '1', ha='center', va='center', fontsize=14, color='white', fontweight='bold', zorder=6)

    # Step 2: git push
    ax.annotate('', xy=(8.8, 4.3), xytext=(7.6, 3.2),
                arrowprops=dict(arrowstyle='->', color='#1976d2', lw=3))
    ax.text(9.6, 3.6, 'git push', ha='center', va='center', fontsize=16, color='#1976d2', fontweight='bold')
    circle2 = plt.Circle((9.6, 4.0), 0.25, color='#1976d2', zorder=5)
    ax.add_patch(circle2)
    ax.text(9.6, 4.0, '2', ha='center', va='center', fontsize=14, color='white', fontweight='bold', zorder=6)

    # Step 3: PR (origin -> upstream:drift) - dashed
    ax.annotate('', xy=(5.3, 5.5), xytext=(6.7, 5.5),
                arrowprops=dict(arrowstyle='->', color='#7b1fa2', lw=3, linestyle='dashed'))
    ax.text(6, 5.15, 'PR to drift-torch', ha='center', va='center', fontsize=18, color='#7b1fa2', fontweight='bold')
    circle3 = plt.Circle((6, 5.85), 0.25, color='#7b1fa2', zorder=5)
    ax.add_patch(circle3)
    ax.text(6, 5.85, '3', ha='center', va='center', fontsize=14, color='white', fontweight='bold', zorder=6)

    plt.tight_layout(pad=0.1)
    plt.savefig('img/git_workflow_case2_will.png', dpi=150, bbox_inches='tight', facecolor='white', pad_inches=0.1)
    plt.close()
    print("Saved img/git_workflow_case2_will.png")


if __name__ == '__main__':
    case1_prototyping()
    case2_feature_branch()
    case2_will_joins()
    case3_quick_fixes()
    print("\nAll diagrams generated!")
