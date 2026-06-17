import pygame
import random
import sys

# Inicializa o Pygame
pygame.init()

# Constantes
LARGURA = 400
ALTURA = 600
VELOCIDADE_JOGO = 5
VELOCIDADE_QUEDA = 0.5
FORCA_PULO = -12
ESPACO_CANOS = 130

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (34, 139, 34)
AMARELO = (255, 255, 0)
VERMELHO = (255, 0, 0)
AZUL_CLARO = (135, 206, 235)

# Configurar tela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

# Fonte
fonte_grande = pygame.font.Font(None, 72)
fonte_pequena = pygame.font.Font(None, 36)


class Passaro:
    def __init__(self):
        self.x = 50
        self.y = ALTURA // 2
        self.largura = 34
        self.altura = 24
        self.velocidade = 0
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)
    
    def pular(self):
        self.velocidade = FORCA_PULO
    
    def atualizar(self):
        # Aplicar gravidade
        self.velocidade += VELOCIDADE_QUEDA
        self.y += self.velocidade
        self.rect.y = self.y
        
        # Limitar movimento vertical
        if self.y < 0:
            self.y = 0
            self.velocidade = 0
        if self.y + self.altura > ALTURA:
            return False  # Colidiu com o chão
        return True
    
    def desenhar(self, surface):
        # Desenhar o passáro como um retângulo amarelo
        pygame.draw.ellipse(surface, AMARELO, self.rect)
        # Desenhar olho
        pygame.draw.circle(surface, PRETO, (self.x + 25, self.y + 8), 3)


class Cano:
    def __init__(self, x):
        self.x = x
        self.largura = 50
        self.altura_cano = random.randint(100, 300)
        self.passou = False
        
        # Posições dos canos (superior e inferior)
        self.cano_superior_rect = pygame.Rect(self.x, 0, self.largura, self.altura_cano)
        self.cano_inferior_rect = pygame.Rect(
            self.x,
            self.altura_cano + ESPACO_CANOS,
            self.largura,
            ALTURA - (self.altura_cano + ESPACO_CANOS)
        )
    
    def atualizar(self):
        self.x -= VELOCIDADE_JOGO
        self.cano_superior_rect.x = self.x
        self.cano_inferior_rect.x = self.x
    
    def desenhar(self, surface):
        pygame.draw.rect(surface, VERDE, self.cano_superior_rect)
        pygame.draw.rect(surface, VERDE, self.cano_inferior_rect)
        # Desenhar bordas dos canos
        pygame.draw.rect(surface, (0, 100, 0), self.cano_superior_rect, 3)
        pygame.draw.rect(surface, (0, 100, 0), self.cano_inferior_rect, 3)
    
    def esta_fora(self):
        return self.x + self.largura < 0


class Jogo:
    def __init__(self):
        self.passaro = Passaro()
        self.canos = []
        self.pontuacao = 0
        self.executando = True
        self.game_over = False
        self.contador_canos = 0
    
    def criar_cano(self):
        novo_cano = Cano(LARGURA)
        self.canos.append(novo_cano)
    
    def atualizar(self):
        if self.game_over:
            return
        
        # Atualizar passáro
        if not self.passaro.atualizar():
            self.game_over = True
        
        # Criar novos canos
        self.contador_canos += 1
        if self.contador_canos > 90:  # Criar cano a cada 90 frames
            self.criar_cano()
            self.contador_canos = 0
        
        # Atualizar canos
        for cano in self.canos:
            cano.atualizar()
            
            # Verificar colisão com o passáro
            if cano.cano_superior_rect.colliderect(self.passaro.rect) or \
               cano.cano_inferior_rect.colliderect(self.passaro.rect):
                self.game_over = True
            
            # Contar pontos ao passar pelo cano
            if cano.x < self.passaro.x < cano.x + cano.largura and not cano.passou:
                cano.passou = True
                self.pontuacao += 1
        
        # Remover canos que saíram da tela
        self.canos = [cano for cano in self.canos if not cano.esta_fora()]
    
    def desenhar(self):
        # Fundo
        tela.fill(AZUL_CLARO)
        
        # Desenhar chão
        pygame.draw.line(tela, (139, 69, 19), (0, ALTURA - 1), (LARGURA, ALTURA - 1), 3)
        
        # Desenhar canos
        for cano in self.canos:
            cano.desenhar(tela)
        
        # Desenhar passáro
        self.passaro.desenhar(tela)
        
        # Desenhar pontuação
        texto_pontos = fonte_pequena.render(f"Pontos: {self.pontuacao}", True, PRETO)
        tela.blit(texto_pontos, (10, 10))
        
        # Desenhar tela de game over
        if self.game_over:
            # Fundo semi-transparente
            overlay = pygame.Surface((LARGURA, ALTURA))
            overlay.set_alpha(200)
            overlay.fill(PRETO)
            tela.blit(overlay, (0, 0))
            
            # Texto game over
            texto_game_over = fonte_grande.render("GAME OVER", True, VERMELHO)
            texto_pontos_final = fonte_pequena.render(
                f"Pontos: {self.pontuacao}",
                True,
                BRANCO
            )
            texto_reiniciar = fonte_pequena.render(
                "Pressione ESPAÇO para recomeçar ou ESC para sair",
                True,
                BRANCO
            )
            
            tela.blit(
                texto_game_over,
                (LARGURA // 2 - texto_game_over.get_width() // 2, ALTURA // 2 - 100)
            )
            tela.blit(
                texto_pontos_final,
                (LARGURA // 2 - texto_pontos_final.get_width() // 2, ALTURA // 2)
            )
            tela.blit(
                texto_reiniciar,
                (LARGURA // 2 - texto_reiniciar.get_width() // 2, ALTURA // 2 + 80)
            )
        
        pygame.display.flip()
    
    def reiniciar(self):
        self.passaro = Passaro()
        self.canos = []
        self.pontuacao = 0
        self.game_over = False
        self.contador_canos = 0
    
    def processar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.executando = False
            
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    if self.game_over:
                        self.reiniciar()
                    else:
                        self.passaro.pular()
                
                if evento.key == pygame.K_ESCAPE:
                    self.executando = False
    
    def executar(self):
        while self.executando:
            self.processar_eventos()
            self.atualizar()
            self.desenhar()
            clock.tick(60)  # 60 FPS
        
        pygame.quit()
        sys.exit()


# Executar jogo
if __name__ == "__main__":
    jogo = Jogo()
    jogo.executar()
