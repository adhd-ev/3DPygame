import pygame

class Object3d:
    def __init__(self, vertices: list[list[float]], edges: list[list[int]], faces: list[list[int]], pos: list[float], face_colors=None):
        self.vertices = vertices
        self.edges = edges
        self.faces = faces
        self.pos = pos
        self.face_colors = face_colors if face_colors else [(255, 0, 0), (0, 255, 0), (0, 0, 255), 
                                                            (255, 255, 0), (255, 0, 255), (0, 255, 255)]

    def draw(self, surface: pygame.Surface) -> None:
        halfWidth = surface.get_width() / 2
        halfHeight = surface.get_height() / 2
        verts = [[o[u] * 50 + self.pos[u] for u in range(3)] for o in self.vertices]
        
        face_depths = []
        for i, face in enumerate(self.faces):
            avg_z = sum(verts[vertex_idx][2] for vertex_idx in face) / len(face)
            face_depths.append((i, avg_z))
        
        face_depths.sort(key=lambda x: x[1], reverse=True)
        
        for face_idx, _ in face_depths:
            face = self.faces[face_idx]
            color = self.face_colors[face_idx % len(self.face_colors)]
            color_with_alpha = (*color, 64)
            
            points_2d = []
            for vertex_idx in face:
                point_div = verts[vertex_idx][2] / 400
                if point_div == 0:
                    continue
                point_2d = [verts[vertex_idx][0] / point_div + halfWidth, 
                           verts[vertex_idx][1] / point_div + halfHeight]
                points_2d.append(point_2d)
            
            if len(points_2d) > 2:
                polygon_surface = pygame.Surface((surface.get_width(), surface.get_height()), pygame.SRCALPHA)
                pygame.draw.polygon(polygon_surface, color_with_alpha, points_2d)
                surface.blit(polygon_surface, (0, 0))
        
        for edge in self.edges:
            point1Div = verts[edge[0]][2] / 400
            if point1Div == 0: continue
            point2Div = verts[edge[1]][2] / 400
            if point2Div == 0: continue
            point1 = [verts[edge[0]][0] / point1Div + halfWidth, verts[edge[0]][1] / point1Div + halfHeight]
            point2 = [verts[edge[1]][0] / point2Div + halfWidth, verts[edge[1]][1] / point2Div + halfHeight]
            pygame.draw.line(surface, (255, 255, 255), point1, point2)

class Cube(Object3d):
    vertices: list[list[float]] = []
    edges: list[list[int]] = []
    faces: list[list[int]] = []
    
    def __init__(self, pos: list[float], face_colors=None) -> None: 
        super().__init__(Cube.vertices, Cube.edges, Cube.faces, pos, face_colors)