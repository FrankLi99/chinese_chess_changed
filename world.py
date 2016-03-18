__author__ = 'lenovo'
image_board_filename = "material/board.gif"
image_CH_filename = "material/OOS.gif"
image_RC_filename = "material/RR.gif"
image_RH_filename = "material/RN.gif"
image_RG_filename = "material/RA.gif"
image_RM_filename = "material/RB.gif"
image_RK_filename = "material/RK.gif"
image_RR_filename = "material/RP.gif"
image_RF_filename = "material/RC.gif"

image_BC_filename = "material/BR.gif"
image_BH_filename = "material/BN.gif"
image_BG_filename = "material/BA.gif"
image_BM_filename = "material/BB.gif"
image_BK_filename = "material/BK.gif"
image_BR_filename = "material/BP.gif"
image_BF_filename = "material/BC.gif"
from component import *
import pygame
from ApiFunction import Api


class World(object):
    def __init__(self, surface):
        self.image_init()
        self.player_count = 0
        self.AllPosition = []
        self.PixPosition = []
        self.player_array = {}
        self.surface = surface
        self.flag_chosen = 0
        for i in range(9):
            self.AllPosition.append([])
            self.PixPosition.append([])
            for j in range(10):
                self.AllPosition[i].append(None)
                self.PixPosition[i].append((8+41 * i, 7+41 * j))

    def image_init(self):
        self.ch = pygame.image.load(image_CH_filename).convert_alpha()
        self.image_RC = pygame.image.load(image_RC_filename).convert_alpha()
        self.image_RH = pygame.image.load(image_RH_filename).convert_alpha()
        self.image_RG = pygame.image.load(image_RG_filename).convert_alpha()
        self.image_RM = pygame.image.load(image_RM_filename).convert_alpha()
        self.image_RK = pygame.image.load(image_RK_filename).convert_alpha()
        self.image_RR = pygame.image.load(image_RR_filename).convert_alpha()
        self.image_RF = pygame.image.load(image_RF_filename).convert_alpha()

        self.image_BC = pygame.image.load(image_BC_filename).convert_alpha()
        self.image_BH = pygame.image.load(image_BH_filename).convert_alpha()
        self.image_BG = pygame.image.load(image_BG_filename).convert_alpha()
        self.image_BM = pygame.image.load(image_BM_filename).convert_alpha()
        self.image_BK = pygame.image.load(image_BK_filename).convert_alpha()
        self.image_BR = pygame.image.load(image_BR_filename).convert_alpha()
        self.image_BF = pygame.image.load(image_BF_filename).convert_alpha()

    def add_player(self, player):
        if (player.x <= 9) and (player.y <= 10):
            self.AllPosition[player.x][player.y] = player
            self.player_array[player.id] = player
            self.player_count = (self.player_count + 1)
        else:
            print "you can't do that"

    def render(self):
        for player in self.player_array.values():
            player.render(self.surface)

    def get_player(self, mouse_position):
        return self.AllPosition[mouse_position[0]][mouse_position[1]]

    def get_player_chosen(self):
        for player in self.player_array.values():
            if player.flag_chosen == 1:
                return player
            else:
                print "there is no player chosen"

    def del_player(self, player):
        self.AllPosition[player.x][player.y] = None
        del self.player_array[player.id]
        self.player_count = (self.player_count - 1)

    def answer_mouse(self, mouse_position):
        mouse_position_vir = Api.pix_to_position(mouse_position)
        print mouse_position_vir
        if self.flag_chosen == 0:
            if self.AllPosition[mouse_position_vir[0]][mouse_position_vir[1]] is not None:
                player = self.get_player(mouse_position_vir)
                player.flag_chosen = 1
                self.flag_chosen = 1
            else:
                pass
        elif self.flag_chosen == 1:
            player_chosen = self.get_player_chosen()
            player_chosen.change_position(mouse_position_vir[0], mouse_position_vir[1])
            player_chosen.flag_chosen = 0
            self.flag_chosen = 0

    def start_new_game(self):
        rc_1 = PlayerCar(1, (0, 0), self.image_RC, self, "red", self.ch)
        rh_1 = PlayerHorse(2, (1, 0), self.image_RH, self, "red", self.ch)
        rm_1 = PlayerMinister(3, (2, 0), self.image_RM, self, "red", self.ch)
        rg_1 = PlayerGuard(4, (3, 0), self.image_RG, self, "red", self.ch)
        rk = PlayerBox(5, (4, 0), self.image_RK, self, "red", self.ch)
        rg_2 = PlayerGuard(6, (5, 0), self.image_RG, self, "red", self.ch)
        rm_2 = PlayerMinister(7, (6, 0), self.image_RM, self, "red", self.ch)
        rh_2 = PlayerHorse(8, (7, 0), self.image_RH, self, "red", self.ch)
        rc_2 = PlayerCar(9, (8, 0), self.image_RC, self, "red", self.ch)
        rf_1 = PlayerFire(10, (1, 2), self.image_RF, self, "red", self.ch)
        rf_2 = PlayerFire(11, (7, 2), self.image_RF, self, "red", self.ch)
        rr_1 = PlayerRanker(12, (0, 3), self.image_RR, self, "red", self.ch)
        rr_2 = PlayerRanker(13, (2, 3), self.image_RR, self, "red", self.ch)
        rr_3 = PlayerRanker(14, (4, 3), self.image_RR, self, "red", self.ch)
        rr_4 = PlayerRanker(15, (6, 3), self.image_RR, self, "red", self.ch)
        rr_5 = PlayerRanker(16, (8, 3), self.image_RR, self, "red", self.ch)
        self.add_player(rc_2)
        self.add_player(rh_2)
        self.add_player(rm_2)
        self.add_player(rg_2)
        self.add_player(rk)
        self.add_player(rg_1)
        self.add_player(rc_1)
        self.add_player(rh_1)
        self.add_player(rm_1)
        self.add_player(rf_1)
        self.add_player(rf_2)
        self.add_player(rr_1)
        self.add_player(rr_2)
        self.add_player(rr_3)
        self.add_player(rr_4)
        self.add_player(rr_5)
        bc_1 = PlayerCar(21, (0, 9), self.image_BC, self, "black", self.ch)
        bh_1 = PlayerHorse(22, (1, 9), self.image_BH, self, "black", self.ch)
        bm_1 = PlayerMinister(23, (2, 9), self.image_BM, self, "black", self.ch)
        bg_1 = PlayerGuard(24, (3, 9), self.image_BG, self, "black", self.ch)
        bk = PlayerBox(25, (4, 9), self.image_BK, self, "black", self.ch)
        bg_2 = PlayerGuard(26, (5, 9), self.image_BG, self, "black", self.ch)
        bm_2 = PlayerMinister(27, (6, 9), self.image_BM, self, "black", self.ch)
        bh_2 = PlayerHorse(28, (7, 9), self.image_BH, self, "black", self.ch)
        bc_2 = PlayerCar(29, (8, 9), self.image_BC, self, "black", self.ch)
        bf_1 = PlayerFire(30, (1, 7), self.image_BF, self, "black", self.ch)
        bf_2 = PlayerFire(31, (7, 7), self.image_BF, self, "black", self.ch)
        br_1 = PlayerRanker(32, (0, 6), self.image_BR, self, "black", self.ch)
        br_2 = PlayerRanker(33, (2, 6), self.image_BR, self, "black", self.ch)
        br_3 = PlayerRanker(34, (4, 6), self.image_BR, self, "black", self.ch)
        br_4 = PlayerRanker(35, (6, 6), self.image_BR, self, "black", self.ch)
        br_5 = PlayerRanker(36, (8, 6), self.image_BR, self, "black", self.ch)
        self.add_player(bc_2)
        self.add_player(bh_2)
        self.add_player(bm_2)
        self.add_player(bg_2)
        self.add_player(bk)
        self.add_player(bg_1)
        self.add_player(bc_1)
        self.add_player(bh_1)
        self.add_player(bm_1)
        self.add_player(bf_1)
        self.add_player(bf_2)
        self.add_player(br_1)
        self.add_player(br_2)
        self.add_player(br_3)
        self.add_player(br_4)
        self.add_player(br_5)

