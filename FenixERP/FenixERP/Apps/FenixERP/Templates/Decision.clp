(defrule inico
(not (nodo-decision)
(printout t "Es un soldado romano si no")
?esSoldado (read)
=>
()
(assert (esSoldado soldado)))

(defrule nosoldado
(no soldado)
(printout t "Es un soldado romano no")
)

(defrule inico
(not (nodo-decision)
(printout t "Es un soldado romano si no")
?esSoldado (read)
=>
()
(assert (esSoldado soldado)))
