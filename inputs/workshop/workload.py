workload = {
    0: {'equation': 'O[k][b]+=W[k][c]*I[c][b]',  # O should be the name of the output operand
        'loop_dim_size': {'K': 4, 'B': 4, 'C': 4},
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},  # O = partial sum precision
        'core_allocation': 1,
        'spatial_mapping': {'D1': ('K', 4)},  # Must match with the dimensions of core 1
        'temporal_ordering': [('B', 4), ('C', 4)],
        'memory_operand_links': {'O': 'O', 'W': 'I1', 'I': 'I2'}
        }
}
