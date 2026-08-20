local highlights = require("dma_theme.highlights")

local M = {}

function M.setup(opts)
  highlights.setup(opts)
end

M.colors = require("dma_theme.palette")

return M