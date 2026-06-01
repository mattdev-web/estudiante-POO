-- Anti-Aimbot Logic (Server-Side)
local Players = game:GetService("Players")

-- Configuración
local MAX_SNAP_ANGLE = 85 -- Grados máximos de giro por frame (ajustable)
local MAX_HEADSHOT_RATIO = 0.9 -- 90% de headshots activa sospecha
local VIOLATION_THRESHOLD = 5 -- Cuántas veces debe fallar antes de ser expulsado

local playerStats = {}

local function onPlayerDamage(attacker, victim, hitPart)
    if not playerStats[attacker.UserId] then
        playerStats[attacker.UserId] = {headshots = 0, totalHits = 0, violations = 0}
    end
    
    local stats = playerStats[attacker.UserId]
    stats.totalHits += 1
    
    if hitPart.Name == "Head" then
        stats.headshots += 1
    end
    
    -- Verificar ratio de Headshots después de 10 disparos
    if stats.totalHits > 10 then
        local ratio = stats.headshots / stats.totalHits
        if ratio > MAX_HEADSHOT_RATIO then
            stats.violations += 1
            warn(attacker.Name .. " tiene un ratio de headshots sospechoso: " .. ratio)
        end
    end
    
    -- Acción si supera las violaciones
    if stats.violations >= VIOLATION_THRESHOLD then
        attacker:Kick("Detección de comportamiento inusual (Aimbot/Accuracy)")
    end
end

-- Ejemplo de conexión (Debes llamar esto desde tu sistema de armas)
-- RemoteEvent.OnServerEvent:Connect(function(player, target, hitPart) ... end)