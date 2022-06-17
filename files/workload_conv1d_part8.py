workload = {
    0: {'equation': 'O[ox][k]+=W[fx][c][k]*I[ix][c]',
        'dimension_relations': ['ix=1*ox+1*fx'],
        'loop_dim_size': {'OX': 4, 'K': 8, 'C': 3, 'FX': 3},
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'core_allocation': 1,
        'memory_operand_links': {'O': 'O', 'W': 'I1', 'I': 'I2'}
        }
}
