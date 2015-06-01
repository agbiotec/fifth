import cam
import ruleset as rs
import neighborhood as nh

def game_of_life(cell, neighbors):
    """
    Rules of the Game of Life.

    Note we ignore the second component of the neighbors tuples since
    life depends on all neighbors
    """
    total = sum(map(lambda x: int(x[0].value), neighbors))
    if cell.value:
        if total < 2 or total > 3:
            return False
        else:
            return True
    elif total == 3:
        return True
    else:
        return False

if __name__ == '__main__':
    c = cam.CAM(1, (100, 100))
    c.randomize()
    r = rs.Ruleset(rs.Rule.SATISFY)
    n = nh.Neighborhood.moore(c.master.grid, True)
    c.start_plot(50, r, n, game_of_life)