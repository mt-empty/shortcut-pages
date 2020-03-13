# ggplot2

> Source: http://docs.ggplot2.org/current/

$ Geoms
    `geom_abline(geom_hline, geom_vline)
>                                  {{Lines: horizontal, vertical, and specified by slope and intercept.}} 
    `geom_bar(stat_count)          {{Bars, rectangles with bases on x-axis.}} 
    `geom_bin2d(stat_bin2d, stat_bin_2d)
>                                  {{Add heatmap of 2d bin counts.}} 
    `geom_boxplot(stat_boxplot)    {{Box and whiskers plot.}} 
    `geom_contour(stat_contour)    {{Display contours of a 3d surface in 2d.}} 
    `geom_count(stat_sum)          {{Count the number of observations at each location.}} 
    `geom_crossbar(geom_errorbar, geom_linerange, geom_pointrange)
>                                  {{Vertical intervals: lines, crossbars & errorbars.}} 
    `geom_dotplot                  {{Dot Plot.}} 
    `geom_errorbarh                {{Horizontal error bars.}} 
    `geom_freqpoly(geom_histogram, stat_bin)
>                                  {{Histograms and frequency polygons.}} 
    `geom_hex(stat_bin_hex, stat_binhex)
>                                  {{Hexagon binning.}} 
    `geom_map                      {{Polygons from a reference map..}} 
    `geom_quantile(stat_quantile)  {{Add quantile lines from a quantile regression.}} 
    `geom_raster(geom_rect, geom_tile)
>                                  {{Draw rectangles.}} 

$ Statistics
    `stat_ecdf                     {{Empirical Cumulative Density Function}} 
    `stat_ellipse                  {{Plot data ellipses.}} 
    `stat_function                 {{Superimpose a function.}} 
    `stat_identity                 {{Identity statistic.}} 
    `stat_qq(geom_qq)              {{Calculation for quantile-quantile plot.}} 
    `stat_summary_2d(stat_summary2d, stat_summary_hex)
>                                  {{Bin and summarise in 2d (rectangle & hexagons)}} 

$ Coordinate systems
    `coord_cartesian               {{Cartesian coordinates}} 
    `coord_fixed(coord_equal)      {{Cartesian coordinates with fixed relationship between x and y scales.}} 
    `coord_flip                    {{Flipped cartesian coordinates.}} 
    `coord_map(coord_quickmap)     {{Map projections.}} 
    `coord_polar                   {{Polar coordinates}} 
    `coord_trans                   {{Transformed cartesian coordinate system}} 

$ Faceting
    `facet_grid                    {{Lay out panels in a grid.}} 
    `facet_null                    {{Facet specification: a single panel.}} 
    `facet_wrap                    {{Flipped cartesian coordinates.}} 
    `labeller                      {{Generic labeller function for facets.}} 
    `label_bquote                  {{Backquoted labeller}} 

$ Plot Creation
    `ggplot(ggplot.data.frame, ggplot.default)
>                                  {{Create a new ggplot plot.}} 
    `qplot(quickplot)              {{Quick plot}} 
    `autoplot                      {{Create a complete ggplot appropriate to a particular data type.}} 
    `is.ggplot                     {{Reports whether x is a ggplot object.}} 
    `print.ggplot(plot.ggplot)     {{Draw plot on current graphics device.}} 

$ Annotation
    `annotate                      {{Create an annotation layer.}} 
    `annotation_custom             {{Annotation: Custom grob.}} 
    `annotation_logticks           {{Annotation: log tick marks.}} 
    `annotation_map                {{Annotation: maps.}} 
    `annotation_raster             {{Annotation: High-performance rectangular tiling.}} 

$ Scales
    `expand_limits                 {{Expand the plot limits with data.}} 
    `guides                        {{Set guides for each scale.}} 
    `scale_alpha(scale_alpha_continuous, scale_alpha_discrete)
>                                  {{Alpha scales.}} 
    `scale_colour_hue(scale_color_discrete, scale_color_hue, scale_colour_discrete, scale_fill_discrete, scale_fill_hue)
>                                  {{Qualitative colour scale with evenly spaced hues.}} 
    `scale_linetype(scale_linetype_continuous, scale_linetype_discrete)
>                                  {{Scale for line patterns.}} 
    `guide_colourbar(guide_colorbar)
>                                  {{Continuous colour bar guide.}} 
    `update_labels                 {{Update axis/legend labels.}} 

